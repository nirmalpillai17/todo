package db

import (
	"context"
	"database/sql"

	_ "github.com/mattn/go-sqlite3"

	be "github.com/nirmalpillai17/todo/backend"
)

const dbFile string = "todo.db"

const create string = `
CREATE TABLE IF NOT EXISTS tasks (
note TEXT NOT NULL,
time DATETIME NOT NULL,
status INTEGER
);`

const update string = "UPDATE tasks SET note=?, time=?, status=? WHERE rowid=?"

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

	if _, err := db.ExecContext(ctx, create); err != nil {
		return nil, err
	}

	return &DBService{
		db: db,
		ctx: ctx,
	}, nil
}


func (dbs *DBService) CreateRecord(t be.TaskData) (id int64, err error) {
	out, err := dbs.db.ExecContext(dbs.ctx, "INSERT INTO tasks VALUES(?,?,?);", t.Note, t.Time, t.Status)
	if err != nil {
		return 0, err
	}

	id, err = out.LastInsertId()
	if err != nil {
		return id, err
	}
	return id, nil
}

func(dbs *DBService) GetAllRecords() (be.Task, error) {
	rows, err := dbs.db.QueryContext(dbs.ctx, "SELECT rowid, * FROM tasks;")
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	
	task := make(be.Task, 0)
	for rows.Next() {
		var id string
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

func (dbs *DBService) UpdateRecord(t be.Task) (error) {
	for id := range t {
		_, err := dbs.db.ExecContext(dbs.ctx, update, t[id].Note, t[id].Time, t[id].Status, id)
		if err != nil {
			return err
		}
	}
	return nil
}

func (dbs *DBService) DeleteRecord(t be.Task) {
}
