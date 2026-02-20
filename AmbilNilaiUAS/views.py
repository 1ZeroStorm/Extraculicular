from flask import render_template, request, redirect, url_for, flash


def register_routes(app, service, repo):
    @app.route('/')
    def index():
        items = service.list_violations()
        return render_template('index.html', items=items)

    @app.route('/new', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            data = request.form
            service.create_violation(
                name=data.get('name', '').strip(),
                absen=data.get('absen', '').strip(),
                kelas=data.get('kelas', '').strip(),
                violation_type=data.get('violation_type', '').strip(),
                reason=data.get('reason', '').strip(),
                frequency=data.get('frequency', 1)
            )
            flash('Data berhasil ditambahkan', 'success')
            return redirect(url_for('index'))
        return render_template('form.html', item=None)

    @app.route('/view/<int:vid>')
    def view(vid):
        item = repo.get_by_id(vid)
        if not item:
            flash('Data tidak ditemukan', 'warning')
            return redirect(url_for('index'))
        return render_template('view.html', item=item)

    @app.route('/edit/<int:vid>', methods=['GET', 'POST'])
    def edit(vid):
        item = repo.get_by_id(vid)
        if not item:
            flash('Data tidak ditemukan', 'warning')
            return redirect(url_for('index'))
        if request.method == 'POST':
            data = request.form
            service.update_violation(vid,
                                     name=data.get('name', '').strip(),
                                     absen=data.get('absen', '').strip(),
                                     kelas=data.get('kelas', '').strip(),
                                     violation_type=data.get('violation_type', '').strip(),
                                     reason=data.get('reason', '').strip(),
                                     frequency=data.get('frequency', item.get('frequency')))
            flash('Data berhasil diperbarui', 'success')
            return redirect(url_for('index'))
        return render_template('form.html', item=item)

    @app.route('/delete/<int:vid>', methods=['POST'])
    def delete(vid):
        ok = service.delete_violation(vid)
        if ok:
            flash('Data berhasil dihapus', 'success')
        else:
            flash('Gagal menghapus data', 'danger')
        return redirect(url_for('index'))
