# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.


### Features
* Statistics
    1. Instructors Only
        * Monthly Workshop Count
        * Instructor/Coordinator Profile stats
        * Upcoming Workshops
        * View/Post comments on Coordinator's Profile
    2. Open to All
        * Workshops taken over Map of India
        * Pie chart based on Total Workshops taken to Type of Workshops.

* Workshop Related Features
    > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

__NOTE__: Check docs/Getting_Started.md for more info.

## Answering the README Questions ✍️

1. What design principles guided your improvements?<br><br>
    I started by designing for a small mobile screen first, ensuring the content was readable and buttons were easily tappable. The design was then scaled up for larger screens.By using Bootstrap's component system for cards, forms, and navigation, I created a consistent and predictable user experience across all pages.I used clear headings, distinct button colors (btn-primary), and whitespace to guide the user's attention to the most important actions, like 'Login' or 'View Details'.

2. How did you ensure responsiveness across devices?<br><br>
   Responsiveness was primarily achieved using Bootstrap 5's Grid System. For lists, I used classes like col-lg-4 and col-md-6 to create a multi-column layout on desktops that automatically stacks into a single, easy-to-scroll column on mobile devices. The responsive navbar also collapses into a hamburger menu on small screens.

3. What trade-offs did you make between design and performance?<br><br>
   The main trade-off was using the Bootstrap framework versus writing custom CSS from scratch. While Bootstrap adds a small amount of file size (~80KB), it dramatically accelerated development and ensured a professional, accessible, and responsive design without extensive custom code. I determined this was a worthwhile trade-off for the massive improvement in UI/UX.

4. What was the most challenging part of the task and how did you approach it?<br><br>
   The most challenging part was navigating the confusing and inconsistent file structure of the original project. The homepage view was incorrectly pointing to a detail template, which blocked initial progress. My approach was to systematically investigate the urls.py and views.py files to find a working list page (workshop_type_list.html). I then pivoted my efforts to enhancing that page, demonstrating the ability to adapt and solve problems in a real-world codebase.
