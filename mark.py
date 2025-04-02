import cv2
import mediapipe as mp
import os

# ✅ MediaPipe 對應 Dlib 68 的 Index 清單
dlib_68_to_mediapipe = [
    # Jawline
    227, 34, 137, 177, 215, 135, 170, 171, 175, 396, 395, 364, 435, 401, 366, 264, 447,
    # Left eyebrow
    70, 63, 105, 66, 107,
    # Right eyebrow
    336, 296, 334, 293, 300,
    # Nose bridge
    168, 197, 5, 1, 2,
    # Nose bottom
    455, 328, 235, 99,
    # Left eye
    33, 160, 158, 133, 153, 144,
    # Right eye
    362, 385, 387, 263, 373, 380,
    # Outer lips
    76, 39, 37, 0, 267, 269, 306, 321, 314, 17, 84, 91, 61, 291,
    # Inner lips
    86, 15, 316, 82, 13, 312
]

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

    for i in range(914,1000):  
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
            # print(f"[📷] 正在處理第 {frame_count} 幀...")

            try:
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(image_rgb)

                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        for idx in dlib_68_to_mediapipe:
                            landmark = face_landmarks.landmark[idx]
                            x = int(landmark.x * width)
                            y = int(landmark.y * height)
                            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

                out.write(frame)

            except Exception as e:
                print(f"[💥 錯誤] 第 {frame_count} 幀處理失敗：{e}")
                break

        cap.release()
        out.release()
        print(f"📦 完成影片 {i_str}：共 {frame_count} 幀，影片儲存至 {output_path}")
