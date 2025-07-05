

import copy

# --- 第3問の解説プログラム ---

# 問題文の表1（講師担当表 Hyou）を模倣したデータ構造
# Hyou[i][j] は i時限からj時限まで連続で担当する講師の人数を表す
# 問題文の表1は対角要素 Hyou[i][i] のみを示しているが、ここでは2次元配列として表現
# 実際の値は問題文の表1の対角要素を参考に、それ以外は0で初期化
# 便宜上、時限は1から5までとする
initial_hyou = [
    [0, 0, 0, 0, 0, 0],  # 0時限目は使用しない
    [0, 8, 0, 0, 0, 0],  # Hyou[1][1] = 8 (1時限のみ担当)
    [0, 0, 19, 0, 0, 0], # Hyou[2][2] = 19 (2時限のみ担当)
    [0, 0, 0, 19, 0, 0], # Hyou[3][3] = 19 (3時限のみ担当)
    [0, 0, 0, 0, 10, 0], # Hyou[4][4] = 10 (4時限のみ担当)
    [0, 0, 0, 0, 0, 7]   # Hyou[5][5] = 7 (5時限のみ担当)
]

# --- 問1の手続きを再現する関数 ---
def assign_continuous_instructors(hyou_table, kaisi_jigen, ninzu_instructors):
    """
    問1の手続きを再現します。
    ninzu_instructors人の講師がkaisi_jigenとkaisi_jigen+1時限を連続で担当するように、
    hyou_tableを更新します。
    """
    print(f"\n--- 手続き実行: {ninzu_instructors}人の講師が{kaisi_jigen}時限と{kaisi_jigen+1}時限を連続担当 ---")
    print("変更前の Hyou テーブル（一部）:")
    print(f"Hyou[{kaisi_jigen}][{kaisi_jigen}]: {hyou_table[kaisi_jigen][kaisi_jigen]}")
    print(f"Hyou[{kaisi_jigen+1}][{kaisi_jigen+1}]: {hyou_table[kaisi_jigen+1][kaisi_jigen+1]}")
    print(f"Hyou[{kaisi_jigen}][{kaisi_jigen+1}]: {hyou_table[kaisi_jigen][kaisi_jigen+1]}")

    # (03) Hyou[kaisi, kaisi+1] ← ninzu
    hyou_table[kaisi_jigen][kaisi_jigen+1] += ninzu_instructors

    # (04) Hyou[kaisi, kaisi] を ninzu 減らす
    hyou_table[kaisi_jigen][kaisi_jigen] -= ninzu_instructors

    # (05) Hyou[kaisi+1, kaisi+1] を ninzu 減らす
    hyou_table[kaisi_jigen+1][kaisi_jigen+1] -= ninzu_instructors

    print("変更後の Hyou テーブル（一部）:")
    print(f"Hyou[{kaisi_jigen}][{kaisi_jigen}]: {hyou_table[kaisi_jigen][kaisi_jigen]}")
    print(f"Hyou[{kaisi_jigen+1}][{kaisi_jigen+1}]: {hyou_table[kaisi_jigen+1][kaisi_jigen+1]}")
    print(f"Hyou[{kaisi_jigen}][{kaisi_jigen+1}]: {hyou_table[kaisi_jigen][kaisi_jigen+1]}")
    print(f"総講師数の変化: -{ninzu_instructors}人 (カの考察)")
    return hyou_table

# --- 問2の手続きを再現する関数 ---
def find_min_instructors(hyou_table, hajime_jigen, owari_jigen):
    """
    問2の手続きを再現します。
    hajime_jigenからowari_jigenまで連続で担当可能な講師数の上限（最小値）を計算します。
    """
    print(f"\n--- 手続き実行: {hajime_jigen}時限から{owari_jigen}時限までの連続担当可能な講師数の上限を探索 ---")

    # (03) saisyou ← Hyou[hajime, hajime]
    saisyou = hyou_table[hajime_jigen][hajime_jigen]
    print(f"初期最小値 (Hyou[{hajime_jigen}][{hajime_jigen}]): {saisyou}")

    # (04) i を hajime+1 から owari まで... (ループ)
    for i in range(hajime_jigen + 1, owari_jigen + 1):
        print(f"現在時限 i: {i}, Hyou[i][i]: {hyou_table[i][i]}")
        # (05) もし saisyou > Hyou[i,i] ならば
        if saisyou > hyou_table[i][i]:
            # (06) saisyou ← Hyou[i,i]
            saisyou = hyou_table[i][i]
            print(f"新しい最小値が見つかりました: {saisyou}")
        else:
            print(f"現在の最小値 {saisyou} は Hyou[{i}][{i}] ({hyou_table[i][i]}) より小さいか等しいです。")

    print(f"結果: {hajime_jigen}時限から{owari_jigen}時限まで連続担当可能な講師数の上限は {saisyou}人です。")
    return saisyou

# --- 実行例 ---
if __name__ == "__main__":
    print("--- 第3問 解説プログラム開始 ---")

    # Hyou テーブルの初期状態をコピーして使用
    current_hyou = copy.deepcopy(initial_hyou)
    print("\n初期 Hyou テーブル（対角要素）:")
    for i in range(1, len(current_hyou)):
        print(f"Hyou[{i}][{i}]: {current_hyou[i][i]}")

    # 問1の手続きの例
    # 2時限と3時限を連続で担当する講師を5人割り当てる
    current_hyou = assign_continuous_instructors(current_hyou, 2, 5)

    # 問2の手続きの例
    # 2時限から4時限まで連続担当可能な講師数の上限を調べる
    max_assignable = find_min_instructors(current_hyou, 2, 4)

    print("\n--- 第3問 解説プログラム終了 ---")

