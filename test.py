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

# 建立輸出資料夾根目錄
output_root = "D:/video/frames"
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
        cap = cv2.VideoCapture(input_path)

        if not cap.isOpened():
            print(f"❌ 無法打開影片：{input_path}")
            continue

        # 建立該影片的圖片資料夾
        frame_output_dir = os.path.join(output_root, i_str)
        os.makedirs(frame_output_dir, exist_ok=True)

        frame_count = 0
        saved_count = 0

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

                filename = f"frame_{frame_count:05d}.jpg"
                filepath = os.path.join(frame_output_dir, filename)

                success = cv2.imwrite(filepath, frame)
                if success:
                    saved_count += 1
                    print(f"[✅ 已儲存] {filepath}")
                else:
                    print(f"[❌ 寫入失敗] {filepath}")

            except Exception as e:
                print(f"[💥 錯誤] 第 {frame_count} 幀處理失敗：{e}")
                break

        cap.release()
        print(f"📦 完成影片 {i_str}：共 {frame_count} 幀，成功儲存 {saved_count} 張")