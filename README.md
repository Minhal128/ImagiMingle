<h1 align="center" id="title">ImagiMingle : A Random Image Generator App 🖼️🖨️</h1>


<p align="center"><img src="https://socialify.git.ci/Minhal128/ImagiMingle/image?description=1&font=Rokkitt&forks=1&language=1&logo=https%3A%2F%2Fimgv3.fotor.com%2Fimages%2Fshare%2Fvarious-random-images-in-all-types-from-fotor-random-image-generator.jpg&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light"></p>

<p>I am thrilled to announce the development of my first Python application, ImagiMingle: a sophisticated Random Image Generator App leveraging the Unsplash API. This innovative tool is designed to provide users with a dynamic experience by generating random images in real-time. Users can explore a wide array of images, select their favorites, and engage with them by liking or disliking their choices. The application also offers the functionality to download images in high definition, ensuring that users have access to high-quality visuals. I am eager to see how this tool can be further enhanced and invite contributions to improve its features and functionality.<p/> 


<h2>🔎 Project Preview</h2>

<img src="https://imgur.com/ZY5kBg9.jpg" alt="Image Description">

<h1 align="center" id="title">Disclaimer</h1>
<p>This application, ImagiMingle, is a Python-based Random Image Generator that utilizes the Unsplash API to fetch and display images. While the application is designed to provide a user-friendly experience, it is important to note the following:

<li>API Usage: This application relies on the Unsplash API, and its functionality is subject to changes in the API's terms of service and rate limits. Ensure you have a valid API key and adhere to Unsplash’s usage guidelines.</li>

<li>Error Handling: Although error handling is included, issues such as network errors, API rate limits, or unexpected data formats may affect functionality. Users are encouraged to report any issues encountered.</li>

<li>Data Privacy: The application does not collect personal data. However, be cautious when downloading and storing images to ensure compliance with copyright laws and Unsplash’s licensing terms.</li>

<li>Dependencies: The application requires external libraries, including requests, tkinter, PIL, and ttkbootstrap. Ensure these dependencies are installed and updated to their compatible versions.</li>

<li>No Warranty: This application is provided "as is" without any warranties or guarantees. The author is not responsible for any damages or issues arising from the use of this application.</li>

Please use this software responsibly and in accordance with applicable laws and guidelines.

.</p>
<h2>🧐 Features</h2>

Our project ImagiMingle offers a range of functionalities designed to enhance the user experience with image generation and management. Key features include:
<ul>
  <li>Real-Time Image Generation: Leverages the Unsplash API to fetch and display random images based on user-selected categories in real-time.</li>
  <li>Dynamic Categories: Users can choose from a diverse set of categories, including Food, Animals, People, Marvel, Art, Technology, Vehicles, Moon, Sky, and more</li>
  <li>Image Selection: Users can view and select their favorite images from a generated set, with the ability to like or dislike each image.</li>
  <li>HD Image Download: Provides an option to download high-definition images for offline use or personal collection.</li>
  <li>Intuitive GUI: Features a user-friendly graphical interface built with Tkinter and ttkbootstrap, including buttons for generating images, liking/disliking, downloading, and exiting the application.</li>
  <li>Responsive Design: Designed to fit various screen sizes with a layout that adjusts to user interactions, ensuring a seamless experience across different devices.</li>
  <li>Error Handling and Notifications: Includes robust error handling to manage issues like network errors and API rate limits, with user-friendly notifications to keep users informed.</li>
  <li>Category-Based Generation: Users can start image generation with a selected category, making it easy to focus on specific types of images.</li>
  <li>Save Preferences: Allows users to select and save their favorite images, providing a personalized experience and easy access to previously liked images.</li>
</ul>
<img src="https://imgur.com/JxMKC3D.jpg" alt="E-LOCKS Features">

  
<h2>🛠 Installation Steps:</h2>

<p>1. Clone the repository</p>

```bash
    git clone https://github.com/Minhal128/ImagiMingle.git
```

<p>2. Install & Run python Language & its modules</p>

```bash Modules to Install
 pip install pillow 
 pip install tkinter
 pip install ttkbootstrap

```bash
 # Run the executable 
python3 imagi_mingle.py
or 
python imagi_mingle.py

```

<h2 align="center">Working </h2>
<p>
<h3><li>Modules Used</li></h3>
<ul>
  <li>requests</li>
  <li>io</li>
  <li>tkinter</li>
  <li>Pillow (PIL)</li>
  <li>ttkbootstrap</li>
</ul>  

</p>
<h3><li>Unsplash API: Your Gateway to Stunning Random Images</li></h3>
<li>Unsplash API</li>
-Purpose: Provides access to high-quality, random images based on specific categories.
-Endpoint: https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=YOUR_API_KEY
<li>Key Features:</li>
-Query Parameter: query={category} specifies the image category.
-Orientation: landscape specifies the image orientation.
-API Key: client_id=YOUR_API_KEY is required for authentication.


<h3><li>SimpleEncryption Class</li></h3>

A simple encryption class is defined to encrypt and decrypt user data using a XOR-based encryption method.</p>

<h3><li>Image Generator Functionality</li></h3>

<li>display_image(category): Fetches a random image from Unsplash based on the selected category and updates the GUI with the image.</li>
<li>like_image() and unlike_image(): Placeholder functions to like or dislike the current image.</li>
<li>download_image(): Saves the current image to a user-specified file path.</li>
<li>start_generation(): Triggers the image generation process based on the selected category.</li>

 </p>

<h3><li>GUI Components</li></h3>
-Dropdown Menu: Allows users to select an image category.
-Generate Button: Fetches and displays a new image based on the selected category.
-Like Button: Enables users to like the displayed image.
-Unlike Button: Enables users to dislike the displayed image.
-Download Button: Allows users to download the current image.
-Image Display Label: Shows the fetched image.
</p>

<h3><li>GUI Layout</li></h3>
-Uses tkinter for creating the window and arranging widgets.
-Applies styles and themes with ttkbootstrap for a modern look.
</p>


<img src ="https://imgur.com/lopeYO9.png">

<h2>⚠️Limitations</h2>
<li>API Rate Limits</li>
<li>Error Handling</li>
<li>No Authentication for Likes/Dislikes</li>
<li>Limited Image Resizing Options:</li>
<li>No Advanced Search Options</li>

<h2>🔮Future Enhancements</h2>
<li>User Authentication and Profile Management</li>
<li>Customizable Image Resizing</li>
<li>Advanced Search and Filtering</li>
<li>Cross-Platform Compatibility</li>
<li>ntegration with Other APIs</li>
<p>

<h2>What I learn?</h2>
<ul>
  <li>
    Basic GUI Development with Tkinter: How to create a graphical user interface using Tkinter, including setting up the main window, adding buttons, and handling user interactions.
  </li>
  
  <li>
    Integration with External APIs: How to interact with the Unsplash API to fetch and display images, including constructing API requests, handling JSON responses, and managing API keys.
  </li>
  
  <li>
    Handling Images with PIL: How to use the Python Imaging Library (PIL) to open, manipulate, and display images in a Tkinter application.
  </li>
  
  <li>
    Using ttkbootstrap for Styling: How to apply modern styles to Tkinter widgets using ttkbootstrap, including configuring button styles and themes.
  </li>

  <li>
   Managing Application State: How to manage application state and update the UI based on user actions, such as enabling/disabling buttons and displaying images.
  </li>
</ul>
<img src="https://imgur.com/a3Mckks.png">
  
<h2>💖Hope you Like our work!</h2>

This project needs a ⭐ from you. Don't forget to leave a star ⭐
