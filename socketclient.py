import websocket
import threading
import time

def on_message(ws, message):
    print("Received:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(10000):
            time.sleep(0.01)  # to prevent flooding the server with messages
            message = f"Hello {i}"
            ws.send(message)
            print("Sent:", message)
        time.sleep(1)  # wait for server to send responses
        ws.close()
        print("Thread terminating...")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8765/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
