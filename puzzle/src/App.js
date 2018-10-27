import React, { Component } from 'react';
import Board from './Board.js';
import Details from './Details.js';
import './App.css';
const axios = require('axios');

export default class App extends Component{

    constructor(props){
        super(props)
        this.state = {
            steps: [[0,0,0,0,0,0,0,0,0]],
            currentState: 0,
            input:[0,0,0,0,0,0,0,0,0],
            costOfPath:0,
            expandedNodes:0,
            depth:0,
            runningTime:0
        }
        this.next = this.next.bind(this);
        this.prev = this.prev.bind(this);
        this.handleBlur = this.handleBlur.bind(this);
        this.solve = this.solve.bind(this);
        this.hasNext = this.hasNext.bind(this);
        this.playAll = this.playAll.bind(this);
        this.pause = this.pause.bind(this);
    }

    playAll(){
        this.setState({
            timer:setInterval(this.next, 500)
        });
    }

    pause(){
        clearInterval(this.state.timer);
    }

    hasNext(){
        if(this.state.currentState < this.state.steps.length - 1){
            return true;
        }
        return false;
    }

    next(){
        if(this.state.currentState < this.state.steps.length - 1){
            this.setState({
                currentState: this.state.currentState + 1
            });
            return
        }
        this.pause();
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
      	let checkArr = [0,0,0,0,0,0,0,0,0,0];
      	for(let i = 0 ; i < 9 ; i++){
      		checkArr[this.state.input[i]]++;
      		if(checkArr[this.state.input[i]] > 1){
      			alert('Error in cell (' + Math.floor(i/3) +', '+ i%3 + ') of the input array 2 cells with number '+ this.state.input[i]);
            this.refs.solve_btn.removeAttribute("disabled");
      			return;
      		}
          if(this.state.input[i] < 0 || this.state.input[i] >= 9){
      			alert('Invalid number ' + this.state.input[i] + ' in cell (' + Math.floor(i/3) +', '+ i%3 + ') of the input array');
            this.refs.solve_btn.removeAttribute("disabled");
            return;
      		}
      	}

        let x = this
        axios.get('/solve', {
            params:{
                algorithm:opt,
                input:[x.state.input]
            },
            timeout: 50000
        })
        .then( (response) => {
            this.setState({
                steps:response.data.steps,
                currentState:0,
                costOfPath:response.data.cost,
                expandedNodes:response.data.nodes_expanded,
                depth:response.data.search_depth,
                runningTime:response.data.time
            })
            if(this.state.costOfPath === -1){
              alert('This puzzle is unsolvable as it contains odd number of inversions, Try another initial puzzle')
            }
            console.log(this.state.steps);
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
                    <div className="col-6">
                        <div className="input-group">
                            <select ref="algorithm" className="custom-select" id="inputGroupSelect04">
                                <option defaultValue value="BFS">BFS</option>
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
                    <div className="col-3">
                        <nav aria-label="Page navigation example pull-left">
                            <ul className="pagination">
                                <li className="page-item">
                                    <a className="page-link" onClick={this.pause}>Pause</a>
                                </li>
                                <li className="page-item active">
                                    <a className="page-link" onClick={this.playAll}>Run</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                    <div className="col-3">
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
                        <label>{this.state.currentState}</label>
                    </div>
                </div>
                <div className="row">
                    <div className="col-6">
                        <Details costOfPath={this.state.costOfPath}
                         expandedNodes={this.state.expandedNodes} depth={this.state.depth} runningTime={this.state.runningTime}/>
                    </div>
                </div>
            </div>

        );
    }

}
