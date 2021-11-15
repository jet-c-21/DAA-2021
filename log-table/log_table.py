import math
import pandas as pd


def get_log_val(base, antilog, rounded=True) -> float:
    log_val = math.log(antilog, base)
    if rounded:
        return round(log_val, 2)
    else:
        return log_val


def gen_log_df(base_start=2, base_end=10, antilog_start=2, antilog_end=10, rounded=True) -> pd.DataFrame:
    columns = [i for i in range(antilog_start, antilog_end + 1)]
    df = pd.DataFrame(columns=columns)

    for b in range(base_start, base_end + 1):
        row_record = list()
        for al in range(antilog_start, antilog_end + 1):
            log_val = get_log_val(b, al, rounded)
            row_record.append(log_val)

        df.loc[len(df)] = row_record

    df.index += base_start

    return df


def gen_log_table(fp=None, file_type='csv', base_start=2, base_end=10, antilog_start=2, antilog_end=10, rounded=True):
    if not fp:
        fp = f"log_table_{base_start}_{base_end}_{antilog_start}_{antilog_end}"

        if file_type == 'csv':
            fp += '.csv'
        else:
            fp += '.xlsx'

    log_df = gen_log_df(base_start, base_end, antilog_start, antilog_end, rounded)

    if file_type == 'csv':
        log_df.to_csv(fp)
    else:
        log_df.to_excel(fp)


if __name__ == '__main__':
    gen_log_table()
    gen_log_table(file_type='xlsx')
