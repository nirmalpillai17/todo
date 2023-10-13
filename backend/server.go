package backend

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/gorilla/mux"
)

type handleServer struct {
	db DBHandler
}

func NewHttpServer(a string, db DBHandler) *http.Server {
	hs := &handleServer{
		db: db,
	}

	r := mux.NewRouter()
	s := r.PathPrefix("/todo").Subrouter()
	s.HandleFunc("/nr", hs.handleCreateRecord).Methods("POST")
	s.HandleFunc("/gr", hs.handleGetAllRecords).Methods("GET")
	s.HandleFunc("/ur", hs.handleUpdateRecord).Methods("POST")

	return &http.Server{
		Addr:         a,
		Handler:      s,
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}
}

func (hs handleServer) handleCreateRecord(w http.ResponseWriter, r *http.Request) {
	var td TaskData
	if err := json.NewDecoder(r.Body).Decode(&td); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	id, err := hs.db.CreateRecord(td)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Fprint(w, id)
	return
}

func (hs handleServer) handleGetAllRecords(w http.ResponseWriter, r *http.Request) {
	t, err := hs.db.GetAllRecords()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	json.NewEncoder(w).Encode(t)
	return
}

func (hs handleServer) handleUpdateRecord(w http.ResponseWriter, r *http.Request) {
	task := Task{}
	if err := json.NewDecoder(r.Body).Decode(&task); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	if err := hs.db.UpdateRecord(task); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}
