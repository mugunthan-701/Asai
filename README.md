
---

## 🔧 Setup & Requirements  

### 1️⃣ Prerequisites  
- **Windows OS** (with Microsoft PowerPoint installed).  
- **Mathematica** (for running the script).  
- **PowerShell** (pre-installed on Windows).  
- **A Gesture Recognition System** (e.g., OpenCV, MediaPipe, or Leap Motion) that writes detected gestures to `slide.txt`.  

### 2️⃣ How to Run  
1. Ensure **PowerPoint is installed** and accessible.  
2. Place your **PowerPoint file** at `E:\DevFolioHack1\Presentation.pptx`.  
3. Ensure your **gesture system writes gestures** (OPEN_HAND, CLOSE_FIST, SWIPE_RIGHT, SWIPE_LEFT) to `slide.txt`.  
4. Run the **Mathematica script** (`main_script.nb`).  
5. Perform gestures to control the slides!  

---

## 🎯 Commands & Gestures  

| **Gesture**      | **Action**                         | **Console Output**                           |
|-----------------|---------------------------------|------------------------------------------|
| `OPEN_HAND`     | Opens PowerPoint Presentation | `Detected: OPEN_HAND → Starting Presentation` |
| `CLOSE_FIST`    | Closes PowerPoint             | `Detected: CLOSE_FIST → Closing Presentation` |
| `SWIPE_RIGHT`   | Moves to Next Slide           | `Detected: SWIPE_RIGHT → Next Slide` |
| `SWIPE_LEFT`    | Moves to Previous Slide       | `Detected: SWIPE_LEFT → Previous Slide` |



## 🤖 Future Improvements  
🔹 **Real-time Hand Tracking** for better responsiveness.  
🔹 **Voice Control Integration** for hands-free operation.  
🔹 **Support for Additional Gestures** like pause, annotate, or zoom.  

---


💡 **Developed by:** Team MENBO 🚀  
