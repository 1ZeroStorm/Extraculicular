from typing import Callable, Optional, List, Dict

STATUS_MAP = {1: 'Peringatan', 2: 'Wajib Lapor', 3: 'Alpha', 4: 'Panggil Orang Tua', 5: 'DO'}


class ViolationRepository:
    """DB operations for violations using a provided `get_connection` callable.

    `get_connection()` should return a mysql.connector connection.
    """

    def __init__(self, get_connection: Callable[[], object]):
        self.get_connection = get_connection

    def _row_to_dict(self, row: Optional[Dict]) -> Optional[Dict]:
        if not row:
            return None
        row['status'] = STATUS_MAP.get(row.get('frequency', 1), 'Tindakan Lain')
        return row

    def get_all(self) -> List[Dict]:
        conn = self.get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute('SELECT * FROM violations ORDER BY id DESC')
            rows = cur.fetchall()
            return [self._row_to_dict(r) for r in rows]
        finally:
            cur.close()
            conn.close()

    def get_by_id(self, vid: int) -> Optional[Dict]:
        conn = self.get_connection()
        try:
            cur = conn.cursor(dictionary=True)
            cur.execute('SELECT * FROM violations WHERE id = %s', (vid,))
            row = cur.fetchone()
            return self._row_to_dict(row)
        finally:
            cur.close()
            conn.close()

    def create(self, **kwargs) -> Optional[Dict]:
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO violations (name, absen, kelas, violation_type, reason, frequency) VALUES (%s,%s,%s,%s,%s,%s)',
                (kwargs.get('name'), kwargs.get('absen'), kwargs.get('kelas'), kwargs.get('violation_type'), kwargs.get('reason'), kwargs.get('frequency'))
            )
            conn.commit()
            lastid = cur.lastrowid
            return self.get_by_id(lastid)
        finally:
            cur.close()
            conn.close()

    def update(self, vid: int, **kwargs) -> Optional[Dict]:
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            parts = []
            values = []
            for k, v in kwargs.items():
                parts.append(f"{k} = %s")
                values.append(v)
            if not parts:
                return self.get_by_id(vid)
            values.append(vid)
            sql = 'UPDATE violations SET ' + ', '.join(parts) + ' WHERE id = %s'
            cur.execute(sql, tuple(values))
            conn.commit()
            return self.get_by_id(vid)
        finally:
            cur.close()
            conn.close()

    def delete(self, vid: int) -> bool:
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM violations WHERE id = %s', (vid,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            cur.close()
            conn.close()
