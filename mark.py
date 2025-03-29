import cv2
import mediapipe as mp
import os
from mediapipe.python.solutions.face_mesh_connections import (
    FACEMESH_LEFT_EYE,
    FACEMESH_RIGHT_EYE,
    FACEMESH_NOSE,
    FACEMESH_LIPS,
)

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# 建立輸出影片資料夾
output_root = "D:\\video\\original_sequences\\marked_youtube"
os.makedirs(output_root, exist_ok=True)

# 初始化 FaceMesh 模型
with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    for i in range(3):
        i_str = str(i).zfill(3)
        print(f"\U0001f5bc️ 處理影片 {i_str}")

        input_path = f'D:/video/original_sequences/youtube/raw/videos/{i_str}.mp4'
        output_path = os.path.join(output_root, f"{i_str}.mp4")

        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            print(f"❌ 無法打開影片：{input_path}")
            continue

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            print(f"[📷] 正在處理第 {frame_count} 幀...")

            try:
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(image_rgb)

                # 僅繪製眼睛、鼻子、嘴巴輪廓
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        target_connections = [
                            FACEMESH_LEFT_EYE,
                            FACEMESH_RIGHT_EYE,
                            FACEMESH_NOSE,
                            FACEMESH_LIPS,
                        ]

                        for connection_group in target_connections:
                            mp_drawing.draw_landmarks(
                                image=frame,
                                landmark_list=face_landmarks,
                                connections=connection_group,
                                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                                connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1)
                            )

                out.write(frame)

            except Exception as e:
                print(f"[💥 錯誤] 第 {frame_count} 幀處理失敗：{e}")
                break

        cap.release()
        out.release()
        print(f"📦 完成影片 {i_str}：共 {frame_count} 幀，影片儲存至 {output_path}")