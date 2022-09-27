## Example Package

## Installation

#### From Local

```shell```

pip install PackagePandasExample-0.0.1-py3-none-any.whl

## Example:


```python
import pandas as pd
from PackagePandasExample.SpecialMethods import doubleDataFrame

testFrame = pd.DataFrame()
testFrame['ID'] = [1,2,3]
testFrame['Color'] = ['Red', 'Blue', 'Green']

testFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Green</td>
    </tr>
  </tbody>
</table>
</div>




```python
dblTestFrame = doubleDataFrame(testFrame)
dblTestFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>ID</th>
      <th>Color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>Green</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>3</td>
      <td>Green</td>
    </tr>
  </tbody>
</table>
</div>


