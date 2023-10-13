package main

import (
	"context"
	"fmt"
	"log"

	"github.com/nirmalpillai17/todo/backend"
	"github.com/nirmalpillai17/todo/db"
)

func main() {

	task_db, err := db.NewDBService(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	/*
		task_db.CreateRecord(backend.Task{Note: "This is bullshit", Time: time.Now(), Status: 1})

		records, err := task_db.GetAllRecords()
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(records)
		j, err := json.Marshal(records)
		if err != nil {
			log.Fatal(err)
		}
		os.Stdout.Write(j)
	*/

	fmt.Println("Listening on port 8080")

	srv := backend.NewHttpServer(":8080", task_db)
	srv.ListenAndServe()
}
