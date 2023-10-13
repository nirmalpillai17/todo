package backend

import "github.com/gorilla/mux"

func NewToDoRouter() {
	r := mux.NewRouter()
	s := r.PathPrefix("/todo/api").Subrouter()
	s.HandleFunc("/nr", DBSizeHandler)
}
