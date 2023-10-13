package backend

import "time"

type Task map[string]TaskData

type TaskData struct {
	Note   string    `json:"note"`
	Time   time.Time `json:"time"`
	Status int       `json:"status"`
}

type DBHandler interface {
	CreateRecord(t TaskData) (int64, error)
	GetAllRecords() (Task, error)
	UpdateRecord(t Task) error
}

type ConfigHandler interface {
	ReadConfig() error
	SetDefault(key string, value string) error
}
