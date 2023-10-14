package db

import (
	"context"
	"database/sql"

	_ "github.com/mattn/go-sqlite3"

	be "github.com/nirmalpillai17/todo/backend"
)

const dbFile string = "todo.db"

const qcreate string = `
CREATE TABLE IF NOT EXISTS tasks (
note TEXT NOT NULL,
time DATETIME NOT NULL,
status INTEGER
);`

const qselect string = "SELECT rowid, * FROM tasks;"

const qinsert string = "INSERT INTO tasks VALUES(?,?,?);"

const qupdate string = "UPDATE tasks SET note=?, time=?, status=? WHERE rowid=?"

const qdelete string = "DELETE FROM tasks WHERE rowid=?"

type DBService struct {
	db *sql.DB
	ctx context.Context
}

func NewDBService(ctx context.Context) (*DBService, error) {
	db, err := sql.Open("sqlite3", dbFile)
	if err != nil {
		return nil, err
	}

	db.SetConnMaxLifetime(0)
	db.SetMaxIdleConns(1)
	db.SetMaxOpenConns(1)

	if _, err := db.ExecContext(ctx, qcreate); err != nil {
		return nil, err
	}

	return &DBService{
		db: db,
		ctx: ctx,
	}, nil
}


func (dbs *DBService) CreateRecord(td be.TaskData) (be.Id, error) {
	out, err := dbs.db.ExecContext(dbs.ctx, qinsert, td.Note, td.Time, td.Status)
	if err != nil {
		return 0, err
	}
	
	id, err := out.LastInsertId()
	if err != nil {
		return 0, err
	}
	return be.Id(id), nil
}

func(dbs *DBService) GetAllRecords() (be.Task, error) {
	rows, err := dbs.db.QueryContext(dbs.ctx, qselect)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	
	task := make(be.Task, 0)
	for rows.Next() {
		var id be.Id
		var td be.TaskData
		if err := rows.Scan(&id, &td.Note, &td.Time, &td.Status); err != nil {
			return nil, err
		}
		task[id] = td
	}

	if err := rows.Err(); err != nil {
		return nil, err
	}
	return task, nil
}

func (dbs *DBService) UpdateRecord(t be.Task) error {
	for id := range t {
		_, err := dbs.db.ExecContext(dbs.ctx, qupdate, t[id].Note, t[id].Time, t[id].Status, id)
		if err != nil {
			return err
		}
	}
	return nil
}

func (dbs *DBService) DeleteRecord(id be.Id) error {
	_, err := dbs.db.ExecContext(dbs.ctx, qdelete, id)
	if err != nil {
		return err
	}
	return nil
}
