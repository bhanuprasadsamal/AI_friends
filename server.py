from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # Correct path for the script
        script_path = r"C:\Users\BHANU\Desktop\AI_assistant\Bhanu's_assistant.py"
        
        # Run the script using subprocess
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        
        # Return the script output as JSON
        return jsonify({"output": result.stdout})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
