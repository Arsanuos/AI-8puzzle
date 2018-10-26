import React, { Component } from 'react';
import Board from './Board.js';
const axios = require('axios');

export default class App extends Component{

    constructor(props){
        super(props)
        this.state = {
            steps: [[0,0,0,0,0,0,0,0,0]],
            currentState: 0,
            input:[0,0,0,0,0,0,0,0,0]
        }
        this.next = this.next.bind(this);
        this.prev = this.prev.bind(this);
        this.handleBlur = this.handleBlur.bind(this);
        this.solve = this.solve.bind(this);
    }

    next(){
        if(this.state.currentState < this.state.steps.length - 1){
            this.setState({
                currentState: this.state.currentState + 1
            });
        }
    }

    prev(){
        if(this.state.currentState > 0){
            this.setState({
                currentState: this.state.currentState - 1
            });
        }
    }

    solve(){
        let sel = this.refs.algorithm;
        var opt = sel.options[sel.selectedIndex].value;

        // disable the button until we return from the request
        this.refs.solve_btn.setAttribute("disabled", "disabled");

        // Make a request for a user with a given ID
        let x = this
        axios.get('/solve', {
            params:{
                algorithm:opt,
                input:[x.state.input]
            },
            timeout: 5000
        })
        .then( (response) => {
            this.setState({
                steps:response.data.steps,
                currentState:0
            })
            console.log(this.state.steps);
            this.render();
            // enable the button after the response
            this.refs.solve_btn.removeAttribute("disabled");
        })
        .catch( (error) => {
            if(error.code == 'ECONNABORTED'){
                alert('Timeout as the Solution is very long, Try another initial puzzle or use another algorithm')
            }
            else{
                alert("Try again");
            }
            console.log(error.message)
            // enable the button after the response
            this.refs.solve_btn.removeAttribute("disabled");
        })

    }

    handleBlur(e){
        let rowNumber = Number(e.target.dataset.row);
        let colNumber = Number(e.target.dataset.col);
        //validate if not number.
        let val = Number(e.target.value);
        let tmpInput = this.state.input;
        tmpInput[3*rowNumber+colNumber] = val;
        this.setState({
            input:tmpInput
        });
        console.log(this.state.input);
    }

    render(){

        return(
            <div className="container">
                <div className="row">
                    <div className="col">
                        <Board handleBlur={this.handleBlur} />
                    </div>
                    <div className="col">
                        <Board data={this.state.steps[this.state.currentState]} disabled="disabled"/>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <div className="input-group">
                            <select ref="algorithm" className="custom-select" id="inputGroupSelect04">
                                <option defaultValue>Select Algorithm</option>
                                <option value="BFS">BFS</option>
                                <option value="DFS">DFS</option>
                                <option value="A start (Manhatten)">A start (Manhatten)</option>
                                <option value="A start (Euclidean)">A start (Euclidean)</option>
                            </select>
                            <div className="input-group-append">
                                <button ref="solve_btn" className="btn btn-primary" type="button" onClick={this.solve}>
                                  Find Path
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <nav aria-label="Page navigation example">
                            <ul className="pagination justify-content-end">
                                <li className="page-item">
                                <a className="page-link" onClick={this.prev}>Previous</a>
                                </li>
                                <li className="page-item">
                                <a className="page-link" onClick={this.next}>Next</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>

        );
    }

}
