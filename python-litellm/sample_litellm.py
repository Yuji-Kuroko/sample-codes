import litellm
import os
import argparse
from dotenv import load_dotenv
import pdb

# .envファイルから環境変数を読み込む
load_dotenv()

def generate_text(prompt: str) -> str:
    try:
        response = litellm.completion(
            model="gemini/gemini-1.5-flash", # or gpt-4o
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='Generate text using GPT-4')
    parser.add_argument('prompt', type=str, help='Input prompt for text generation')
    args = parser.parse_args()

    # APIキーの確認
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your API key based on .env.example")
        return

    # テキスト生成の実行
    result = generate_text(args.prompt)
    
    if result:
        print("Generated response:")
        print(result)
    else:
        print("Failed to generate response")

if __name__ == "__main__":
    main()
