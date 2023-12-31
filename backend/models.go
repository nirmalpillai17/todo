package backend

import "time"

type Task map[Id]TaskData

type Id string

type TaskData struct {
	Note   string    `json:"note"`
	Time   time.Time `json:"time,omitempty"`
	Status int       `json:"status"`
}

type DBHandler interface {
	CreateRecord(td TaskData) (Id, error)
	GetAllRecords() (Task, error)
	UpdateRecord(id Id, td TaskData) error
	DeleteRecord(id Id) error
}

type ConfigHandler interface {
	ReadConfig() error
	SetDefault(key string, value string) error
}
