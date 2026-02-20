from typing import Optional, Dict


class ViolationService:
    def __init__(self, repo):
        self.repo = repo

    def list_violations(self):
        return self.repo.get_all()

    def create_violation(self, name, absen, kelas, violation_type, reason, frequency):
        frequency = max(1, min(5, int(frequency or 1)))
        return self.repo.create(name=name, absen=absen, kelas=kelas,
                                violation_type=violation_type, reason=reason,
                                frequency=frequency)

    def update_violation(self, vid, **kwargs) -> Optional[Dict]:
        if 'frequency' in kwargs:
            kwargs['frequency'] = max(1, min(5, int(kwargs['frequency'] or 1)))
        return self.repo.update(vid, **kwargs)

    def delete_violation(self, vid) -> bool:
        return self.repo.delete(vid)
