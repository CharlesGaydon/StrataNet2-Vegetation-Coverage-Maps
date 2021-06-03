import re
import numpy as np
import pandas as pd


def stats_txt_to_csv(args):
    df = pd.DataFrame(
        columns=[
            "pl_id",
            "pred_veg_b",
            "pred_sol_nu",
            "pred_veg_moy",
            "pred_veg_h",
            "vt_veg_b",
            "vt_sol_nu",
            "vt_veg_moy",
            "vt_veg_h",
        ]
    )
    i = 0
    with open(args.stats_path) as f:
        for line in f:
            if line.startswith("POINT_") or line.startswith("Releve_"):
                print(line)
                results = re.search("([^\s]+)  Pred \[(.*?)] GT \[(.*?)]", line)
                pl_id = results.group(1)
                pred_values = np.fromstring(results.group(2), dtype=float, sep=" ")
                gt_values = np.fromstring(results.group(3), dtype=float, sep=" ")[:4]
                print(pl_id)
                print(pred_values)
                print(gt_values)
                # print(np.append((np.asarray([pl_id]), pred_values, gt_values), 0))
                df.loc[i] = [pl_id] + list(pred_values) + list(gt_values)
                i += 1

    df.to_csv(path_or_buf=args.stats_path.replace(".txt", ".csv"), index=False, sep=",")
