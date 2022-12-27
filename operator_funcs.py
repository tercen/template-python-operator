from tercen.client import context as ctx
import pandas as pd

def calc_mean(tercenCtx:ctx.TercenContext) -> pd.DataFrame:
    df = tercenCtx.select(['.y', '.ci', '.ri'])

    df = df.groupby(['.ci','.ri'], as_index=False).mean()
    df = df.rename(columns={".y":"mean"})

    return df
