# The MIT License (MIT)
#
# Copyright (c) 2016 Todd Treece for Adafruit Industries
# Copyright (c) 2018 Brent Rubell for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
`adafruitio_00_publish.py` - Publishes an increasing value to an Adafruit IO Feed
====================================================
* Author(s): Todd Treece, Brent Rubell
"""
import time
# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'YOUR ADAFRUIT IO USERNAME'
ADAFRUIT_IO_KEY = 'YOUR ADAFRUIT IO KEY'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# set up the "counter" feed
feed = Feed(name="counter")
# create the "counter" feed
response = aio.create_feed(feed)

count = 0
while True:
    print("Sending -> ", count)
    aio.send_data('counter', count)

    # increment the count by 1
    count += 1

    # Adafruit IO is rate limited for publishing to a feed, so a delay is required
    # let's wait 3 seconds between each iteration of this loop
    time.sleep(3)
    