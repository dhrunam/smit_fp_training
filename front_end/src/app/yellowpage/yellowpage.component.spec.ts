import { ComponentFixture, TestBed } from '@angular/core/testing';

import { YellowpageComponent } from './yellowpage.component';

describe('YellowpageComponent', () => {
  let component: YellowpageComponent;
  let fixture: ComponentFixture<YellowpageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [YellowpageComponent]
    });
    fixture = TestBed.createComponent(YellowpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
