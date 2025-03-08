import cv2
import mediapipe as mp
import time

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Inicializar la cámara
cap = cv2.VideoCapture(0)

def countdown(seconds):
    """Realiza una cuenta regresiva de los segundos especificados"""
    for i in range(seconds, 0, -1):
        ret, frame = cap.read()
        if not ret:
            break
        
        # Mostrar el contador en la pantalla
        cv2.putText(frame, f"Preparate en: {i}", (50, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Deteccion de Dedos", frame)
        cv2.waitKey(1000)

def count_raised_fingers(landmarks):
    """Cuenta cuántos dedos están levantados"""
    # Puntos de referencia de las puntas de los dedos
    finger_tips = [4, 8, 12, 16, 20]  # pulgar, índice, medio, anular, meñique
    count = 0
    
    # Verificar pulgar
    if landmarks[4].x < landmarks[3].x:  # Punta del pulgar vs base
        count += 1
    
    # Verificar otros dedos (índice a meñique)
    for tip in finger_tips[1:]:
        if landmarks[tip].y < landmarks[tip-2].y:  # Comparar punta con articulación inferior
            count += 1
            
    return count

def main():
    print("Iniciando programa...")
    
    # Realizar cuenta regresiva de 3 segundos
    countdown(3)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convertir la imagen a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Procesar la imagen con MediaPipe
        results = hands.process(rgb_frame)
        
        # Si se detecta una mano
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibujar los puntos de la mano
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Contar dedos levantados
                finger_count = count_raised_fingers(hand_landmarks.landmark)
                
                # Mostrar el conteo en pantalla
                cv2.putText(frame, f"Dedos levantados: {finger_count}", (50, 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Mostrar el frame
        cv2.imshow("Deteccion de Dedos", frame)
        
        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()