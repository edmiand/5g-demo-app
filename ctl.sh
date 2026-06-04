#!/usr/bin/env bash
set -uo pipefail

PID_FILE=".chainlit.pid"
LOG_FILE="chainlit.log"
CMD=".venv/bin/python start.py"

_pid() { [[ -f "$PID_FILE" ]] && cat "$PID_FILE"; }
_running() { local p; p=$(_pid); [[ -n "$p" ]] && kill -0 "$p" 2>/dev/null; }

start() {
    if _running; then
        echo "Already running (PID $(_pid))"
        return
    fi
    nohup $CMD >> "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    echo "Started (PID $!  —  logs: $LOG_FILE)"
}

stop() {
    if ! _running; then
        echo "Not running"
        rm -f "$PID_FILE"
        return
    fi
    local pid; pid=$(_pid)
    kill "$pid"
    rm -f "$PID_FILE"
    echo "Stopped (PID $pid)"
}

status() {
    if _running; then
        echo "Running (PID $(_pid))"
    else
        echo "Stopped"
    fi
}

case "${1:-help}" in
    start)   start ;;
    stop)    stop ;;
    restart) stop; sleep 1; start ;;
    status)  status ;;
    logs)    tail -f "$LOG_FILE" ;;
    *)       echo "Usage: $0 {start|stop|restart|status|logs}" ;;
esac
