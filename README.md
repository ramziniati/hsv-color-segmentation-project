# hsv-color-segmentation-project 🎨
Do you see my profile picture? I manipulated it using image processing algorithms.

My workflow was as follows:

📸 First, I read the image
🎨 Then I converted it to the HSV color space to enable masking
🖱️ I used a click_event function to pick pixels from the background and extract their HSV values
🎯 From these values, I defined the target color range

After that, I applied a masking function to isolate the background region 🧼, then modified it to shift the color toward yellow 🟡. Finally, I converted the image back to RGB 🔄 to display the result.

Through this project, I learned how masking works for color manipulation, as well as the fundamentals of the HSV model (Hue, Saturation, Value) 🧠. I also explored the relationship between HSL and HSV, where hue remains consistent while saturation and luminance/value are adjusted mathematically.

And this marks my first image processing project 🚀
