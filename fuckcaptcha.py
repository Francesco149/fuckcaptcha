from pathlib import Path
import fuckcaptcha_data

async def bypass_detections(page):
  fuck_js = Path(fuckcaptcha_data.__file__).parent / "fuck.js"
  with open(fuck_js) as f:
    await page.evaluateOnNewDocument(f.read())
