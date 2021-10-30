<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AKapaldo/WhatsForDinner">
    <img src="images/WhatsForDinner.png" alt="Logo">
  </a>

<h3 align="center">Cyber Tools</h3>

  <p align="center">
    What's for dinner is an Alexa skill designed to help choose a randomly choose a place to eat dinner.
    <br />
    <a href="https://github.com/AKapaldo/WhatsForDinner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AKapaldo/WhatsForDinner">View Demo</a>
    ·
    <a href="https://github.com/AKapaldo/WhatsForDinner/issues">Report Bug</a>
    ·
    <a href="https://github.com/AKapaldo/WhatsForDinner/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#version-history">Version History</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!--->
[![Product Name Screen Shot][product-screenshot]](https://example.com)
--->
What's for Dinner is an Alexa skill that can be run in AWS Lambda to accept requests via your personal Amazon account. To run the skill you will need a Google API account and an Amazon Alexa Developer account.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Google API](https://console.cloud.google.com/)
* [Amazon Alexa Developer](https://developer.amazon.com/en-US/alexa)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You will need to create a Google Cloud account to get an API key and you will also need an Amazon Alexa Developer account.

### Prerequisites

Some tools require Python. To install:
* Create a <a href="https://console.cloud.google.com/">Google Cloud account</a> and under "APIs and Services", click on "Credentials", and then "Create Credentials". You will want to restrict your key and use the below APIs.
    * Places API
    * Geocoding API
    * Geolocation API
* You will also need to create an <a href="https://developer.amazon.com/en-US/alexa">Amazon Alexa Developer account</a> and put the included files under Lambda in the "Code" section of your skill.

  

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/AKapaldo/WhatsForDinner.git
   ```
2. In your <a href="https://console.cloud.google.com/">Google Cloud account</a>, under "APIs and Services", click on "Credentials", and then "Create Credentials". You will want to restrict your key and use the below APIs.
    * Places API
    * Geocoding API
    * Geolocation API
3. In your <a href="https://developer.amazon.com/en-US/alexa">Amazon Alexa Developer account</a>, put the files you cloned above under Lambda in the "Code" section of your skill.
    * <img src="/images/lambdadinner.png>
4. You will need to update lines 19 to 23 on the lambda.py function.
    * <img src="/images/lines.png>
    * Line 19 is your Google API key from above (DO NOT SHARE THIS KEY WITH ANYONE!)
    * Line 20 is your favorite places. e.g. ['Chick Fil A', 'McDonald\'s', 'Subway', 'Firehouse Subs', 'Papa Johns'] 
    * Line 21 is your favorite types. e.g. ["Italian", "Mexican", "Burgers", "Fine Dining", "Chinese", "Japanese", "Pizza"]
    * Line 22 is your Latitude and Longitude. e.g. (40.730610, -73.935242)
    * Line 23 is the radius in meters from the Latitude and Longitude the program will search. Max is 50,000. The default is 16,000 or about 10 miles. You can adjust as needed.
5. In the "Build" section, you will need to create phrases to say to use the skill. e.g. Pick three {FoodType} restaurants.<br>You will need Intents for the following.
    * PickTwo
    * PickThree
    * OneFav
    * TwoFav
    * ThreeFav

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once you have everything in place, you can ask your Alexa device to use the skill based on what you called in the developer console and how you configured the intents. For example, in mine we can use:
```sh
Alexa, ask What`s for Dinner to pick two restaurants from my favorites.
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- VERSION -->
## Version History

- v1.0: Created What's for Dinner
    - v1.1: Added Google Places API search
    - v1.2: Added additional intents to pull from the favorites list for 1 or 2 choices in addition to the existing option of 3.

See the [open issues](https://github.com/AKapaldo/WhatsForDinner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>
---->


<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andrew Kapaldo - [@KapaldoA](https://twitter.com/kapaldoa)

Project Link: [https://github.com/AKapaldo/WhatsForDinner](https://github.com/AKapaldo/WhatsForDinner)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>
---->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AKapaldo/WhatsForDinner.svg?style=for-the-badge
[contributors-url]: https://github.com/AKapaldo/WhatsForDinner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AKapaldo/WhatsForDinner.svg?style=for-the-badge
[forks-url]: https://github.com/AKapaldo/WhatsForDinner/network/members
[stars-shield]: https://img.shields.io/github/stars/AKapaldo/WhatsForDinner.svg?style=for-the-badge
[stars-url]: https://github.com/AKapaldo/WhatsForDinner/stargazers
[issues-shield]: https://img.shields.io/github/issues/AKapaldo/WhatsForDinner.svg?style=for-the-badge
[issues-url]: https://github.com/AKapaldo/WhatsForDinner/issues
[license-shield]: https://img.shields.io/github/license/AKapaldo/WhatsForDinner.svg?style=for-the-badge
[license-url]: https://github.com/AKapaldo/WhatsForDinner/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/andrew-kapaldo
[product-screenshot]: images/whatsfordinner.png
