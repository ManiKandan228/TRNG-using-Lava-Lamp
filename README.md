# TRNG-using-Lava-Lamp

## Contributors
[![DonBoscoBlaise](https://github.com/DonBoscoBlaiseA.png?size=50)](https://github.com/DonBoscoBlaiseA) [DonBoscoBlaise](https://github.com/DonBoscoBlaiseA)
[![Mainkandan](https://github.com/ManiKandan228.png?size=50)](https://github.com/ManiKandan228) [Manikandan](https://github.com/ManiKandan228)

## Abstract
The research investigates using a lava lamp as a True Random Number Generator (TRNG). Unlike conventional TRNGs, the lava lamp uses the chaotic motion of wax blobs to generate randomness, showing promise for encryption and simulations. Algorithms extract random numbers from video recordings of the wax movement. Initial findings indicate genuine randomness due to the unpredictable wax behavior. Future work will refine algorithms, explore applications, and enhance the lava lamp TRNG as a reliable, cost-effective alternative to traditional generators. This project explores this approach, highlighting its potential in encryption and simulations.

## Objective
 * Evaluate the randomness and unpredictability of lava lamp wax movements as a source for generating encryption codes
 * Identify potential applications and use cases for encryption codes generated using the lava lamp TRNG in various industries and sectors.

## Proposed System
We generate random numbers using lava lamp footage as the entropy source. The footage is processed frame-by-frame to capture the wax blobs' movement. Each frame is converted from colorized to grayscale to reduce data complexity, as grayscale uses a single channel. The grayscale frames are then converted to bytes, which are hashed using the SHA-256 algorithm, producing fixed-size hash values (256 bits). These hash values are converted to hexadecimal and used for cryptographic encryption.

## Architecture Diagram

![image](https://github.com/ManiKandan228/TRNG-using-Lava-Lamp/assets/119160414/39719f28-f854-4efd-b595-eef501eed3a0)

## Lava Lamp SetUp
![image](https://github.com/ManiKandan228/TRNG-using-Lava-Lamp/assets/119160414/9b30ec3f-f75e-426f-85ae-642175d34f76)

## Output
![image](https://github.com/ManiKandan228/TRNG-using-Lava-Lamp/assets/119160414/cad60bf8-fcc4-4b44-8f77-02651cde9e92)

## Conclusion
In conclusion, using a lava lamp as a True Random Number Generator (TRNG) offers a promising and innovative approach to random number generation. Preliminary findings indicate that the unpredictable motion of the lava lamp's wax blobs can reliably produce true randomness. This method challenges traditional approaches and shows potential for diverse applications across industries, from secure financial transactions to scientific simulations and communication protocols.
