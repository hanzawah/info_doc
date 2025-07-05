# AI関連ルールとGitHub Pages公開ガイドライン

## 1. AI関連ドキュメントの配置
- AIに関するドキュメントはすべて`AI_doc`フォルダ内に配置すること。
- 各ドキュメントはMarkdown形式（`.md`）で作成し、分かりやすいファイル名を付けること。

## 2. GitHub Pages公開ルール
- 本リポジトリの`Doc`ディレクトリ以下のコンテンツは、GitHub Pagesを通じてHTMLとして公開される。
- `Doc`ディレクトリ内に配置されたMarkdownファイルは、自動的にHTMLに変換され、ウェブ上で閲覧可能となる。
- `Doc`ディレクトリ直下には、公開コンテンツのルートとなる`index.html`または`README.md`を配置することが推奨される。

## 3. 教育コンテンツの取り扱い
- 教育目的のコンテンツは、`docs`ディレクトリ内の適切なサブフォルダに分類して配置すること。
- コンテンツは明確で簡潔な表現を心がけ、図やコードスニペットなどを活用し、理解を深める工夫をすること。

## 4. ナビゲーションルール
- 各サブフォルダ内の`index.html`ファイルからは、ルートの`docs/index.html`への明確な戻るリンクを設置すること。
- ユーザーがサイト内を迷わずに移動できるよう、直感的なナビゲーションを心がけること。

## 5. ファイル構造の例

```
info_doc/
├── AI_doc/
│   └── ai_rules.md
├── docs/
│   ├── index.html
│   ├── static/
│   │   └── index-styles.css
│   ├── center2025/
│   ├── center2012/
│   ├── basic_ai/
│   │   └── index.html
│   ├── info-math/
│   │   ├── index.html
│   │   └── bin-dec-conversion.html
│   └── images/
│       └── image.png
``` 