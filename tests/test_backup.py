import contextlib
import os
import shutil

from zhihubackup import backup_zhihu

def test_backup():
    user = "wei-ze-xi-89"
    backup_zhihu(user)
    assert len(os.listdir(os.path.join(user, "answer"))) == 24
    assert len(os.listdir(os.path.join(user, "article"))) == 1
    assert len(os.listdir(os.path.join(user, "question"))) == 3

    # allow failed
    shutil.rmtree(user, ignore_errors=True)
    with contextlib.suppress(FileNotFoundError):
        os.remove("record")

