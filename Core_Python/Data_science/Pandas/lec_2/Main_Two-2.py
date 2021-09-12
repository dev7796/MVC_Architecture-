import pandas as pd

html_string = """
<table>
  <thead>
    <tr>
      <th>Programming Language</th>
      <th>Creator</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>Dennis Ritchie</td>
      <td>1972</td>
    </tr>
    <tr>
      <td>Python</td>
      <td>Guido Van Rossum</td>
      <td>1989</td>
    </tr>
    <tr>
      <td>Ruby</td>
      <td>Yukihiro Matsumoto</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
"""

d1 = pd.read_html(html_string)
print(d1)
print()

f1 = open('../../../../Downloads/table3.html', 'r')
d2 = pd.read_html(f1.read())
print(d2)
