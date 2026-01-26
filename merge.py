import pandas as pd
from pathlib import Path
import argparse

def merge_annotations(samples_folder, annotations_file):
    """
    Merges annotations with samples.

    Args:
        samples_folder (str): The path to the folder containing samples.
        annotations_file (str): The path to the file containing annotations.
    """
    adf = pd.read_csv(annotations_file, sep='\t')
    adf.columns = ['annot:' + c if c != 'id' else c for c in adf.columns]

    dfs = []
    for lang in adf['annot:lang'].unique():
        lang_path = Path(samples_folder)
        lang_pat = f'{lang}/*zst' if (lang_path/lang).is_dir() else f'{lang}*zst'
 
        df = pd.concat((pd.read_json(p, lines=True) for p in lang_path.glob(lang_pat)), ignore_index=True)
        dfs.append(df[df.id.isin(adf.id)])

    if not dfs:
        raise ValueError("No objects to concatenate. Check if the samples folder is correct and contains data.")

    df = pd.concat(dfs, ignore_index=True)
    
    rdf = adf.merge(df, how='left', on='id')
    
    assert rdf.text.isnull().sum() == 0, "Text column should not have null values after merge."
    
    rdf.to_json('annotated.jsonl.zst', orient='records', lines=True)
    print("Successfully merged annotations and wrote to annotated.jsonl.zst")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge annotations with samples.')
    parser.add_argument('samples_folder', type=str, help='Folder with samples')
    parser.add_argument('annotations_file', type=str, help='File with annotations')

    args = parser.parse_args()

    merge_annotations(args.samples_folder, args.annotations_file)
