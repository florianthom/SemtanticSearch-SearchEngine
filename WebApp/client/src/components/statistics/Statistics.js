import React, {Component} from "react";
import {Container} from "reactstrap";
import MostOftenSearchedStatistics from "./MostOftenSearchedStatistics";
import ViewLonger4Seconds from "./ViewLonger4Seconds";

class Statistics extends Component{
    render(){
        return (
            <div>
                <Container>
                    <MostOftenSearchedStatistics />
                    <ViewLonger4Seconds />
                </Container>
            </div>
        );
    }
}

export default Statistics;