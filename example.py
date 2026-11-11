#for a package have to use from to retrieve
from dotenv import load_dotenv
#for library use import
#need this to read the file
import os

#have to load to bring into the environemtn
load_dotenv()

no_longer_a_secret = os.getenv('secret')
print(no_longer_a_secret)