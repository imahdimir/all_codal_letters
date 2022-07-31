##

"""
combines old (82-89) data with new(after 89) data
    """

##

from pathlib import Path
from pathlib import PurePath

import pandas as pd

outpn = Path('comb.prq')
oldpn = Path('82_89.prq')
newpn = Path('after_89.prq')

def make_old_columns_compatible_to_new(df) :
  cols_map = {
      'نماد'    : 'Symbol' ,
      'شرکت'    : 'CompanyName' ,
      'اطلاعیه' : 'Title' ,
      'انتشار'  : 'PublishDateTime' ,
      'پیوست'   : 'AttachmentUrl' ,
      'pgn'     : 'opgn' ,
      }

  df = df.rename(columns = cols_map)

  return df

def main() :

  pass

  ##
  dfo = pd.read_parquet(oldpn)
  dfn = pd.read_parquet(newpn)

  ##
  dfo = make_old_columns_compatible_to_new(dfo)

  ##
  dfn = pd.concat([dfn , dfo])

  ##
  dfn.to_parquet(outpn , index = False)

  ##
  oldpn.unlink()
  newpn.unlink()

##


if __name__ == "__main__" :
  main()
  print(f'{PurePath(__file__).name} Done.')