import paddle
import paddle.nn as nn

from .base_color import *


class SIGGRAPHGenerator(BaseColor):
    def __init__(self, norm_layer=nn.BatchNorm2D, classes=529):
        super(SIGGRAPHGenerator, self).__init__()

        # Conv1
        model1 = [
            nn.Conv2D(4, 64, kernel_size=3, stride=1, padding=1),
        ]
        model1 += [
            nn.ReLU(True),
        ]
        model1 += [
            nn.Conv2D(64, 64, kernel_size=3, stride=1, padding=1),
        ]
        model1 += [
            nn.ReLU(True),
        ]
        model1 += [
            norm_layer(64),
        ]
        # add a subsampling operation

        # Conv2
        model2 = [
            nn.Conv2D(64, 128, kernel_size=3, stride=1, padding=1),
        ]
        model2 += [
            nn.ReLU(True),
        ]
        model2 += [
            nn.Conv2D(128, 128, kernel_size=3, stride=1, padding=1),
        ]
        model2 += [
            nn.ReLU(True),
        ]
        model2 += [
            norm_layer(128),
        ]
        # add a subsampling layer operation

        # Conv3
        model3 = [
            nn.Conv2D(128, 256, kernel_size=3, stride=1, padding=1),
        ]
        model3 += [
            nn.ReLU(True),
        ]
        model3 += [
            nn.Conv2D(256, 256, kernel_size=3, stride=1, padding=1),
        ]
        model3 += [
            nn.ReLU(True),
        ]
        model3 += [
            nn.Conv2D(256, 256, kernel_size=3, stride=1, padding=1),
        ]
        model3 += [
            nn.ReLU(True),
        ]
        model3 += [
            norm_layer(256),
        ]
        # add a subsampling layer operation

        # Conv4
        model4 = [
            nn.Conv2D(256, 512, kernel_size=3, stride=1, padding=1),
        ]
        model4 += [
            nn.ReLU(True),
        ]
        model4 += [
            nn.Conv2D(512, 512, kernel_size=3, stride=1, padding=1),
        ]
        model4 += [
            nn.ReLU(True),
        ]
        model4 += [
            nn.Conv2D(512, 512, kernel_size=3, stride=1, padding=1),
        ]
        model4 += [
            nn.ReLU(True),
        ]
        model4 += [
            norm_layer(512),
        ]

        # Conv5
        model5 = [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model5 += [
            nn.ReLU(True),
        ]
        model5 += [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model5 += [
            nn.ReLU(True),
        ]
        model5 += [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model5 += [
            nn.ReLU(True),
        ]
        model5 += [
            norm_layer(512),
        ]

        # Conv6
        model6 = [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model6 += [
            nn.ReLU(True),
        ]
        model6 += [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model6 += [
            nn.ReLU(True),
        ]
        model6 += [
            nn.Conv2D(512, 512, kernel_size=3, dilation=2, stride=1, padding=2),
        ]
        model6 += [
            nn.ReLU(True),
        ]
        model6 += [
            norm_layer(512),
        ]

        # Conv7
        model7 = [
            nn.Conv2D(512, 512, kernel_size=3, stride=1, padding=1),
        ]
        model7 += [
            nn.ReLU(True),
        ]
        model7 += [
            nn.Conv2D(512, 512, kernel_size=3, stride=1, padding=1),
        ]
        model7 += [
            nn.ReLU(True),
        ]
        model7 += [
            nn.Conv2D(512, 512, kernel_size=3, stride=1, padding=1),
        ]
        model7 += [
            nn.ReLU(True),
        ]
        model7 += [
            norm_layer(512),
        ]

        # Conv7
        model8up = [nn.Conv2DTranspose(512, 256, kernel_size=4, stride=2, padding=1)]
        model3short8 = [
            nn.Conv2D(256, 256, kernel_size=3, stride=1, padding=1),
        ]

        model8 = [
            nn.ReLU(True),
        ]
        model8 += [
            nn.Conv2D(256, 256, kernel_size=3, stride=1, padding=1),
        ]
        model8 += [
            nn.ReLU(True),
        ]
        model8 += [
            nn.Conv2D(256, 256, kernel_size=3, stride=1, padding=1),
        ]
        model8 += [
            nn.ReLU(True),
        ]
        model8 += [
            norm_layer(256),
        ]

        # Conv9
        model9up = [
            nn.Conv2DTranspose(256, 128, kernel_size=4, stride=2, padding=1),
        ]
        model2short9 = [
            nn.Conv2D(128, 128, kernel_size=3, stride=1, padding=1),
        ]
        # add the two feature maps above

        model9 = [
            nn.ReLU(True),
        ]
        model9 += [
            nn.Conv2D(128, 128, kernel_size=3, stride=1, padding=1),
        ]
        model9 += [
            nn.ReLU(True),
        ]
        model9 += [
            norm_layer(128),
        ]

        # Conv10
        model10up = [
            nn.Conv2DTranspose(128, 128, kernel_size=4, stride=2, padding=1),
        ]
        model1short10 = [
            nn.Conv2D(64, 128, kernel_size=3, stride=1, padding=1),
        ]
        # add the two feature maps above

        model10 = [
            nn.ReLU(True),
        ]
        model10 += [
            nn.Conv2D(128, 128, kernel_size=3, dilation=1, stride=1, padding=1),
        ]
        model10 += [
            nn.LeakyReLU(negative_slope=0.2),
        ]

        # classification output
        model_class = [
            nn.Conv2D(256, classes, kernel_size=1, padding=0, dilation=1, stride=1),
        ]

        # regression output
        model_out = [
            nn.Conv2D(128, 2, kernel_size=1, padding=0, dilation=1, stride=1),
        ]
        model_out += [nn.Tanh()]

        self.model1 = nn.Sequential(*model1)
        self.model2 = nn.Sequential(*model2)
        self.model3 = nn.Sequential(*model3)
        self.model4 = nn.Sequential(*model4)
        self.model5 = nn.Sequential(*model5)
        self.model6 = nn.Sequential(*model6)
        self.model7 = nn.Sequential(*model7)
        self.model8up = nn.Sequential(*model8up)
        self.model8 = nn.Sequential(*model8)
        self.model9up = nn.Sequential(*model9up)
        self.model9 = nn.Sequential(*model9)
        self.model10up = nn.Sequential(*model10up)
        self.model10 = nn.Sequential(*model10)
        self.model3short8 = nn.Sequential(*model3short8)
        self.model2short9 = nn.Sequential(*model2short9)
        self.model1short10 = nn.Sequential(*model1short10)

        self.model_class = nn.Sequential(*model_class)
        self.model_out = nn.Sequential(*model_out)

        self.upsample4 = nn.Sequential(
            *[
                nn.Upsample(scale_factor=4, mode="bilinear"),
            ]
        )
        self.softmax = nn.Sequential(
            *[
                nn.Softmax(axis=1),
            ]
        )

    def forward(self, input_A, input_B=None, mask_B=None):
        if input_B is None:
            input_B = paddle.concat((input_A * 0, input_A * 0), axis=1)
        if mask_B is None:
            mask_B = input_A * 0

        conv1_2 = self.model1(
            paddle.concat(
                (self.normalize_l(input_A), self.normalize_ab(input_B), mask_B), axis=1
            )
        )
        conv2_2 = self.model2(conv1_2[:, :, ::2, ::2])
        conv3_3 = self.model3(conv2_2[:, :, ::2, ::2])
        conv4_3 = self.model4(conv3_3[:, :, ::2, ::2])
        conv5_3 = self.model5(conv4_3)
        conv6_3 = self.model6(conv5_3)
        conv7_3 = self.model7(conv6_3)

        conv8_up = self.model8up(conv7_3) + self.model3short8(conv3_3)
        conv8_3 = self.model8(conv8_up)
        conv9_up = self.model9up(conv8_3) + self.model2short9(conv2_2)
        conv9_3 = self.model9(conv9_up)
        conv10_up = self.model10up(conv9_3) + self.model1short10(conv1_2)
        conv10_2 = self.model10(conv10_up)
        out_reg = self.model_out(conv10_2)

        conv9_up = self.model9up(conv8_3) + self.model2short9(conv2_2)
        conv9_3 = self.model9(conv9_up)
        conv10_up = self.model10up(conv9_3) + self.model1short10(conv1_2)
        conv10_2 = self.model10(conv10_up)
        out_reg = self.model_out(conv10_2)

        return self.unnormalize_ab(out_reg)


def siggraph17(pretrained=True):
    model = SIGGRAPHGenerator()
    if pretrained:
        model.set_state_dict(
            paddle.load(
                "6364_MechineLearning/Final/model/pretrain/paddle_siggraph17.pdparams"
            )
        )
    return model
