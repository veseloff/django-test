import classes from "./Expenses.module.css";
import {ResponsiveBar} from '@nivo/bar'
import {compose} from "redux";
import {connect} from "react-redux";
import ExpensesConstructor from "./ExpensesConstructor/ExpensesConstructor";
import {NavLink, withRouter} from "react-router-dom";
import cn from "classnames";
import {setExpensesDataTC} from "../../redux/expensesReducer";
import {useEffect} from "react";

const Expenses = (props) => {
    const id = isNaN(Number(props.match.params.businessTripId))
        ? (props.businessTrip.id || 'new')
        : Number(props.match.params.businessTripId);

    useEffect(() => {
            props.setExpensesDataTC(id);
        },
        // eslint-disable-next-line
        [])

    return (
        <div className={classes.body_container}>
            <div className={classes.first_row}>
                <div>
                    Расходы
                </div>
                <NavLink to={`/business-trips/${id}`} className={cn(classes.button, classes.exit)}>
                    &#8592; {/*todo: exit icon*/}
                </NavLink>
            </div>
            <ResponsiveBar
                data={props.fullExpensesData}
                keys={['Рублей']}
                indexBy="date"
                margin={{top: 50, right: 130, bottom: 50, left: 60}}
                padding={0.3}
                valueScale={{type: 'linear'}}
                indexScale={{type: 'band', round: true}}
                colors={"#1B496C"}
                borderColor={{from: 'color', modifiers: [['darker', 1.6]]}}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'Дни',
                    legendPosition: 'middle',
                    legendOffset: 32
                }}
                axisLeft={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'Расходы',
                    legendPosition: 'middle',
                    legendOffset: -40
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                labelTextColor={"white"}
                legends={[
                    {
                        dataFrom: 'keys',
                        anchor: 'bottom-right',
                        direction: 'column',
                        justify: false,
                        translateX: 120,
                        translateY: 0,
                        itemsSpacing: 2,
                        itemWidth: 100,
                        itemHeight: 20,
                        itemDirection: 'left-to-right',
                        symbolSize: 20,
                    }
                ]}
                barAriaLabel={function (e) {
                    return e.id + ": " + e.formattedValue + " in country: " + e.indexValue
                }}
                height={400}/>
            <div>
                {
                    props.lastExpensesData !== undefined
                        ? props.lastExpensesData.map((expenses, index) =>
                            <ExpensesConstructor expenses={expenses} key={index}/>
                        )
                        : null
                }
            </div>
        </div>
    );
}

const mapStateToProps = (state) => {
    return {
        fullExpensesData: state.expensesData.fullExpensesData,
        lastExpensesData: state.expensesData.lastExpensesData,
        businessTrip: state.businessTripsData.businessTrip,
    }
}

export default compose(connect(mapStateToProps, {setExpensesDataTC}), withRouter)(Expenses);
