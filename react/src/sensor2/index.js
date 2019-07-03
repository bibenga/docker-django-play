import React from 'react';
import {
    fetchUtils, Admin, Resource, ListGuesser, EditGuesser,
    EditButton, ShowButton, Filter,
    List, Datagrid, TextField, EmailField, ArrayField,
    Edit, Create, Show, SimpleShowLayout, SimpleFormIterator,
    SimpleForm, DisabledInput, TextInput, ArrayInput,
    required, minLength, maxLength
} from 'react-admin';

const Sensor2RuleFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn />
        <TextInput label="Code" source="code" />
    </Filter>
);

const Sensor2RuleList = (props) => (
    <List filters={<Sensor2RuleFilter />} sort={{ field: 'code', order: 'ASC' }} {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="code" />
            <TextField source="value_expr" />
            <EditButton />
            <ShowButton />
        </Datagrid>
    </List>
);

const Sensor2RuleShow = (props) => (
    <Show title={<Sensor2RuleTitle />} {...props}>
        <SimpleShowLayout>
            <TextField source="id" />
            <TextField source="code" />
            <TextField source="value_expr" />
        </SimpleShowLayout>
    </Show>
);

const Sensor2RuleTitle = ({ record }) => {
    if (record && record.id) {
        let displayName = record.code;
        return <span>Edit sensor 2 rule {displayName}</span>;
    } else {
        return <span>Create new sensor 2 rule</span>;
    }
}

const validateValueExpr = [required()];

const Sensor2RuleCreate = (props) => (
    <Create title={<Sensor2RuleTitle />} {...props}>
        <SimpleForm>
            <TextInput source="code" />
            <TextInput source="value_expr" validate={validateValueExpr} />
        </SimpleForm>
    </Create>
);

const Sensor2RuleEdit = (props) => (
    <Edit title={<Sensor2RuleTitle />} {...props}>
        <SimpleForm >
            <DisabledInput source="id" />
            <TextInput source="code" />
            <TextInput source="value_expr" validate={validateValueExpr} />
        </SimpleForm>
    </Edit>
);

export { Sensor2RuleList, Sensor2RuleShow, Sensor2RuleCreate, Sensor2RuleEdit };

