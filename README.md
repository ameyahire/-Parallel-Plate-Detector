## Abstract 
This mini-project demonstrates a number plate detection system
using OpenCV and parallel processing techniques. The system captures
video frames, detects number plates, and processes the images in
parallel to improve performance.

## Parallel Processing Method
 In this project, parallel processing is utilized to enhance the performance of num
ber plate detection. The Python multiprocessing module is used to achieve
 this. The main idea is to separate the tasks of frame capturing and plate detec
tion into different processes that run concurrently.

## Why Parallel Processing?
 In a sequential processing approach, the main program captures a frame from
 the video stream, processes it to detect number plates, and then displays the
 result. This sequence of operations can create a bottleneck, especially when
 real-time performance is required. By using parallel processing, we can overlap
 the operations of capturing frames and detecting plates, thus improving the
 throughput and responsiveness of the system

 ## Conclusion
 This project demonstrates the implementation of a number plate detection sys
tem using parallel processing to improve efficiency. By leveraging OpenCV for
 image processing and EasyOCR for text recognition, the system can effectively
 detect and recognize number plates in real-time. The parallel processing ap
proach significantly enhances performance compared to a sequential method,
 making it suitable for applications requiring high throughput and low latency

