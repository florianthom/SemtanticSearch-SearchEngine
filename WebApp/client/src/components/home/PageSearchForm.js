import React from "react";

class Form extends React.Component{
    render(){
        return (
            <div class="searchform">
                <form>
                    <input type="text"/>
                    <button>Search</button>
                </form>
            </div>
        );
    }
}

export default Form;