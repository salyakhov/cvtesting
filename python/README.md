# Install OpenCV
* Mac OS https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/

# Configure environment
mkvirtualenv cvt -p python3
cd ~/.virtualenvs/cvt/lib/python3.6/site-packages/
ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-darwin.so cv2.so

# Python packages
<code>
pip install numpy
pip install imutils
pip install selenium
pip install py4j
</code>

# Chrome Driver
brew cask install chromedriver

