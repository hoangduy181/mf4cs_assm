import pandas as pd

def create_point(lat, lon):
  return f'POINT ({lon} {lat})'

def create_linestring(path):
  line = list(map(lambda point: f'{point[1]} {point[0]}', path))
  return f'LINESTRING ({", ".join(line)})'

def compile_rows(nodemap, path, start, end, algorithm):
    loc_path = []
    loc_path=list(map(lambda x: nodemap[f'{x}'], path))
    pathwkt = create_linestring(loc_path)
    path_row = {'WKT': pathwkt, 'id': f'path-{start}-{end}-{algorithm}'}
    # pathdf = pd.DataFrame([path_row])
    return path_row
    
def compile_csv(dfs, start, end):
    path_rows = []
    for i in range(len(dfs)):
        path_rows.append(dfs[i])
    new_rows_df = pd.DataFrame(path_rows)
    df = pd.DataFrame(columns=['WKT', 'id'])
    df = pd.concat([df, new_rows_df], ignore_index=False)
    df.to_csv(f'solutions./path-{start}-{end}.csv', index = False)

