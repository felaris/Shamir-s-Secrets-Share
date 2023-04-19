# Shamir-s-Secrets-Share
I have tried to create Shamir's Secret Sharing algorithm using Python. 
Shamir's Secret Sharing is a cryptographic algorithm for splitting a secret into multiple shares, 
such that any subset of the shares can be combined to reconstruct the original secret, 
but no subset smaller than the required threshold can do so. 
Check [here](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) for the mathematic formulation.

# Usage
* Clone the repository 
~~~bash 
git clone https://github.com/felaris/Shamir-s-Secrets-Share.git
~~~

* Navigate to the project directory and install dependencies
~~~bash 
cd Shamir-s-Secrets-Share
pip install requirement.txt
~~~
The `script` directory consist of the `preparation.py` and `reconstruct.py` scripts.
The `share.txt` contain the generated secrets.


# Future Work 
- Planning on integrating this into a main vault program.