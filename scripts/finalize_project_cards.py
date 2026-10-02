from pathlib import Path

path = Path('README.md')
text = path.read_text()

old = '''<table align="center" border="1" cellspacing="0" cellpadding="14">
  <tr>
    <td align="center" valign="top" width="350">
      <a href="https://github.com/denoskume/Python-CardGame"><b>Python CardGame</b></a><br><br>
      <a href="https://github.com/denoskume/Python-CardGame"><img src="https://raw.githubusercontent.com/denoskume/Python-CardGame/main/docs/cardgame_demo.gif" width="320" alt="Python CardGame real gameplay demo" /></a><br><br>
      <sub>Event-driven three-card tracking game</sub><br>
      <sub>Pygame · finite-state machine · modular architecture</sub><br>
      <sub>JSON persistence · timed states</sub>
    </td>
    <td align="center" valign="top" width="350">
      <a href="https://github.com/denoskume/monstage"><b>MonStage</b></a><br><br>
      <a href="https://github.com/denoskume/monstage"><img src="https://raw.githubusercontent.com/denoskume/monstage/main/docs/assets/monstage_preview_sanitized.png" width="320" alt="MonStage real application interface" /></a><br><br>
      <sub>Internship discovery, prioritization &amp; application tracking</sub><br>
      <sub>React · TypeScript · authentication</sub><br>
      <sub>Cloudflare Worker · Apps Script · responsive UI</sub>
    </td>
  </tr>
</table>'''

new = '''<p align="center">
  <a href="https://github.com/denoskume/Python-CardGame"><img src="assets/project-cardgame-real-card.png?v=1" width="340" height="340" alt="Python CardGame" /></a>
  &nbsp;&nbsp;
  <a href="https://github.com/denoskume/monstage"><img src="assets/project-monstage-real-card.png?v=1" width="340" height="340" alt="MonStage" /></a>
</p>'''

if old not in text:
    raise SystemExit('Expected project table not found')

path.write_text(text.replace(old, new))
