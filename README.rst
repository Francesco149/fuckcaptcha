bypass reCAPTCHA detection in pyppeteer

note that this does not solve captchas, it's just to bypass the detection
so you can write a bot to solve captchas

this is just a pyppeteer port of https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth
so all credits to them

usage
=========

install fuckcaptcha and pyppeteer

.. code-block:: sh

    pip install fuckcaptcha pyppeteer


run this example and try to do the audio verification. it should work fine
instead of saying your browser is automated.

keep in mind that recaptcha likes to randomly flag ip's and user agents
which might confuse you when testing

also, it's recommended to use a recent chromium build:

linux/mac:

.. code-block:: sh

    PYPPETEER_CHROMIUM_REVISION="706915" python .\fuck.py


windows:

.. code-block:: powershell

    $env:PYPPETEER_CHROMIUM_REVISION="706915"
    python.exe .\fuck.py


fuck.py:

.. code-block:: python

    import asyncio
    from pyppeteer import launch
    import fuckcaptcha as fucking
    import sys

    async def main():
      browser = await launch(headless=False)
      page = await browser.newPage()
      await fucking.bypass_detections(page)
      await page.goto("https://www.google.com/recaptcha/api2/demo")
      while True:
        await asyncio.sleep(1)

    if sys.platform == "win32":
      loop = asyncio.ProactorEventLoop()
    else:
      loop = asyncio.new_event_loop()

    # workaround for KeyboardInterrupt on wangblows
    async def wake_the_fuck_up():
      while True:
        await asyncio.sleep(1)

    loop.create_task(wake_the_fuck_up())
    loop.run_until_complete(main())


license
=========
- fuck.js is MIT licensed: https://github.com/berstend/puppeteer-extra/blob/master/LICENSE
- pyppetteer is MIT licensed: https://github.com/miyakogi/pyppeteer/blob/dev/LICENSE
- my 2 lines of glue code are UNLICENSED: https://unlicense.org/
