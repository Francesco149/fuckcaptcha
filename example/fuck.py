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
