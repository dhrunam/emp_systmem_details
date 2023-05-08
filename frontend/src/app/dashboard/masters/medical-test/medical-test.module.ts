import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MedicalTestRoutingModule } from './medical-test-routing.module';
import { ViewComponent } from './view/view.component';
import { EditComponent } from './edit/edit.component';
import { MaterialModule } from 'src/app/material/material.module';
import { SharedModule } from 'src/app/shared/shared.module';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    ViewComponent,
    EditComponent
  ],
  imports: [
    MaterialModule,
    MedicalTestRoutingModule,
    SharedModule,
    FormsModule,

  ]
})
export class MedicalTestModule { }
