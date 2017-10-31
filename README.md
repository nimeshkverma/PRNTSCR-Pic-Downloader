# PRNTSCR-Pic-Downloader

https://prnt.sc/ allows users to upload screenshots, images etc and share it with other users. PRNTSCR-Pic-Downloader script helps users to download the Images from the weblink.

That is, this utility takes the URL of the Webpage as an Input, Like the one give below.

URL: `https://prnt.sc/h4dhl1`

Visual:

![alt text](https://image.prntscr.com/image/hfTdoKFmSQWTm0nRaHxvvw.png)

Downloads:
 - ![alt text](https://image.prntscr.com/image/On_5afQmRDq2cajLQfApIQ.jpg)

With the unique identifies in its input webpage url as the image name. For eg: `h4dhl1.png` in case of `https://prnt.sc/h4dhl1`

## Prerequisites
- Python 2.7
- Recommended: Any Python Virtual Environment Utility

## Usage

1. Clone the repository move into any of the directory `PRNTSCR-Pic-Downloader` by:

    `cd PRNTSCR-Pic-Downloader`
    
2. If using a virual environment, activate it and run the following command:

    `pip install -r requirements.txt`

3. Run the following command by inserting the correct valus
    ```python
    python prntscr_pic_downloader.py web_url_1 web_url_2 web_url_3 ....
    ```

## Example

Thats if the web url are:
- https://prnt.sc/aaaaa
- https://prnt.sc/bbbbb
- https://prnt.sc/ccccc
- https://prnt.sc/ddddd

Use the command:

    ```python
    python prntscr_pic_downloader.py https://prnt.sc/aaaaa https://prnt.sc/bbbbb https://prnt.sc/ccccc https://prnt.sc/ddddd
    ```

## How to Contribute

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull RequestThe scripts in this
